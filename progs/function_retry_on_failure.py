
import  logging
log =  logging.getLogger()

class Retry:
    """
    class Retry : This will retry the function by 1 time.
    """

    def __init__(self, except_function=None, retry_value=2):
        """
        Retry class : Default retry value is 1

        :param except_function:
        :param retry_value:
        """
        self.except_function = except_function
        self.retry_value = retry_value

    def __call__(self, function):
        """
        Calling function with arguments.
        Default retry is 1.
        Maximum 1 failure is ignored.

        :param function: Foo
        :param args: Foo args
        :param kwargs: Foo kwargs

        :return:
        """

        def inner_func(*args, **kwargs):
            """
            Inner function which executes the actual function and Except function.

            :param args:
            :param kwargs:
            :return:
            """
            for i in range(0, self.retry_value + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    if i == self.retry_value:
                        raise e
                    if self.except_function:
                        self.except_function(*args, **kwargs)
                    log.warning("Try #{} failed with Exception: {}".format(i, e))
                    continue

        return inner_func


def rts():
    x = 2
    y = 0
    j = x / 1
    print(j)

@Retry(except_function = None)
def rt():
    x = 2
    y = 0
    j = x / y
    print(j)



rt()