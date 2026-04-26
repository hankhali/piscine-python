#!/usr/bin/env python3


def main() -> None:
    """Modify each object to match the required greetings, then print them."""
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # Modify values to match the required output
    ft_list[1] = "World!"
    ft_tuple = ("Hello", "United Arab Emirates!")
    ft_set.remove("tutu!")
    ft_set.add("Abu Dhabi!")
    ft_dict["Hello"] = "42Abu Dhabi!"

    print(ft_list)
    print(ft_tuple)

    # Print set deterministically (avoid random set ordering)
    print("{" + ", ".join(repr(x) for x in sorted(ft_set)) + "}")

    print(ft_dict)


if __name__ == "__main__":
    main()
