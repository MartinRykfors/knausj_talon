from talon import cron, Context, ui
from talon.canvas import Canvas
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia.imagefilter import ImageFilter
from talon.types import Rect


ctx = Context()


@ctx.action_class("user")
class GenericNotificationActions:
    def flash_cancel():
        """Flash cancel symbol"""
        flash_square("red")

    def flash_repeat():
        """Flash repeat symbol"""
        flash_square("green")

    def show_as_subtitle(text: str):
        """Display text in the subtitle bar"""
        pass

    def clear_subtitles():
        """Clear the subtitle bar"""
        pass

    def notify_sleep():
        """Notify Talon asleep"""
        flash_square("blue")

    def notify_wake():
        """Notify Talon asleep"""
        flash_square("#00ffff")

    def notify_deprecated():
        """Notify usage of deprecated function"""
        flash_square("#ffa000")


def flash_square(color: str):
    for screen in ui.screens():
        r = screen.rect
        center_x = r.x + r.width / 2
        center_y = r.y + r.height / 2
        flash_rect_at(color, center_x, center_y)


def flash_rect_at(color: str, center_x: int, center_y: int):
    canvas_size = 200
    draw_size = canvas_size - 20
    canvas_rect = Rect(
        center_x - canvas_size / 2,
        center_y - canvas_size / 2,
        canvas_size,
        canvas_size,
    )
    draw_rect = Rect(
        center_x - draw_size / 2,
        center_y - draw_size / 2,
        draw_size,
        draw_size,
    )
    canvas = Canvas.from_rect(canvas_rect)

    def on_draw(c):
        c.paint.imagefilter = ImageFilter.drop_shadow(2, 2, 1, 1, "000000")
        c.paint.style = c.paint.Style.FILL
        c.paint.color = color
        c.draw_rect(draw_rect)

        c.paint.imagefilter = None
        c.paint.style = c.paint.Style.STROKE
        c.paint.color = "black"
        c.draw_rect(draw_rect)

        cron.after("300ms", canvas.close)

    canvas.register("draw", on_draw)
    canvas.freeze()
