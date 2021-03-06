from colors import color


def group(group: dict):
    try:
        active = group["5850"] == 1
        group_id = group["9003"]
        brightness = group["5851"] / 2.55
        group_name = group["9001"]
        print(
            "{} {} - {}, {:.1f}%".format(
                group_id,
                color(group_name, style="bold"),
                color("on", fg="green") if active else color("off", fg="red"),
                brightness,
            )
        )
    except KeyError:
        pass


def bulb(bulb: dict):
    try:
        bulb_id = bulb["9003"]
        bulb_name = bulb["9001"]
        active = bulb["3311"][0]["5850"] == 1
        brightness = bulb["3311"][0]["5851"] / 2.55
        try:
            colour = bulb["3311"][0]["5706"]
            coloured_colour = color(f", #{colour}", f"#{colour}")
        except (KeyError, ValueError):
            colour = "ffffff"
            coloured_colour = ", " + colour
        print(
            " {} {} - {}, {:.1f}%{}".format(
                bulb_id,
                color(bulb_name),
                color("on", fg="green") if active else color("off", fg="red"),
                brightness,
                coloured_colour,
            )
        )
    except KeyError:
        pass
