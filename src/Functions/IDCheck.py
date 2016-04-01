import keyword
import string

alphas = string.ascii_letters + '_'
nums = string.digits
keywords = keyword.kwlist
alphnums = alphas + nums

def idcheck(identifier):
    if len(identifier) == 1:
        if identifier not in alphas:
            print('Invalid : first sybol must be alphabetic or "_" ')
        else:
            print('Okay as a legal identifier')
    else:
        if identifier in keywords:
            print('Invalid : identifier can not be a key word.')
        elif identifier[0] not in alphas:
            print('Invalid : first sybol must be alphabetic or "_"')
        else:
            for otherChar in identifier[1:]:
                if otherChar not in alphnums:
                    print('Invalid: remaining symbols must be alphanumeric!')
                    break
            else:
                print('Okay as a legal identifier')