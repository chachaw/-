# -*- coding: utf-8 -*-
import re


def register_params_check(content):
    """
    TODO: 进行参数检查
    """

    if "username" not in content \
            or not re.match("^[a-zA-Z]+[0-9]+$", content["username"]) \
            or len(content["username"]) < 5 \
            or len(content["username"]) > 12:

        return "username", False

    if "password" not in content \
            or not re.match("^[A-Za-z0-9-_*^]{8,15}$", content["password"]) \
            or not re.search("[A-Z]", content["password"]) \
            or not re.search("[a-z]", content["password"]) \
            or not re.search("[0-9]", content["password"]) \
            or not re.search("[-_*^]", content["password"]):

        return "password", False

    if "nickname" not in content:

        return "nickname", False

    if "url" not in content:
        return "url", False
    else:
        if re.match("https://", content["url"]):
            url = content["url"][8:]
        elif re.match("http://", content["url"]):
            url = content["url"][7:]
        else:
            return "url", False

        if len(url) > 48 or "." not in url:
            return "url", False

        partsOfUrl = url.split(".")

        for part in partsOfUrl:
            if not part \
                    or not re.match(
                        "^[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9]$|^[A-Za-z0-9]$",
                    part):
                return "url", False

        if re.match("^\\d+$", partsOfUrl[-1]):
            return "url", False

    if "mobile" not in content \
            or not re.match("^\\+\\d{2}\\.\\d{12}$", content["mobile"]):
        return "mobile", False

    if "magic_number" not in content or content["magic_number"] is None:
        content["magic_number"] = 0

    if not isinstance(content["magic_number"], int):
        return "magic_number", False

    return "ok", True
