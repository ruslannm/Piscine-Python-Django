def my_sort(d):
    years = []
    for value in d.values():
        if value not in years:
            years.append(value)
    years.sort()
    for y in years:
        musicians = []
        for key, value in d.items():
            if value == y:
                musicians.append(key)
        musicians.sort()
        for m in musicians:
            print(m)        


if __name__ == '__main__':
    d = {
        'Hendrix' : '942', 'Allman' : '1946',
        'King' : '1925', 'Clapton' : '1945',
        'Johnson' : '1911', 'Berry' : '1926',
        'Vaughan' : '1954', 'Cooder' : '1947',
        'Page' : '1944', 'Richards' : '1943',
        'Hammett' : '1962', 'Cobain' : '1967',
        'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947',
        'Ramone' : '1948', 'White' : '1975',
        'Frusciante': '1970', 'Thompson' : '1949',
        'Burton' : '1939',
        }
    my_sort(d)