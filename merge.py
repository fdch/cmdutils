#!/usr/local/bin/python3
"""
Merge one or multiple csv files flattening repeated columns
"""
import csv

def merge_csv_files(filenames, output_path, flatten=True, sep=' '):
    
    data = []
    headers = set()

    # load csv data of all files into data array
    for f in sorted(filenames):
        with open(f) as csvfile:
            csv_data_obj = csv.reader(csvfile)
            csv_list = []
            for i, entry in enumerate(csv_data_obj):
                if i == 0:
                    # add headers to the headers set
                    for h in entry:
                        headers.add(h)
                # add data to the data list
                csv_list.append(entry)
            data.append(csv_list)

    # sort headers
    headers = list(sorted(headers))

    # output the csv file
    with open(output_path, 'w') as f:
        csv_writer = csv.writer(f,)
        csv_writer.writerow(headers)
        for d in data:
            e_heads = d[0] # the headers
            for dd in d[1:]: # the data
                row = []
                if flatten:
                    for h in headers:
                        # keep count of how many columns we found
                        count = e_heads.count(h)
                        if count == 1:
                            row.append(dd[e_heads.index(h)])
                        elif count > 1: # more than one
                            multi_h = ''
                            # store the indices where these cols are located
                            idx = [i for i, x in enumerate(e_heads) if h == x]
                            for i in idx:
                                # append to string with sep char as delimiter
                                multi_h += sep + dd[i]
                            row.append(multi_h)
                        else: # no data for this column, fill as blank
                            row.append('')
                else: # do not flatten, simply overwrite to last value
                    for h in headers:
                        if h in e_heads:
                            row.append(dd[e_heads.index(h)])
                        else:
                            row.append('')
                csv_writer.writerow(row)

if '__main__' in __name__:
    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument('filenames', type=str, nargs="+")
    parser.add_argument('-o', '--output_path', default='output.csv')

    args = parser.parse_args()
    merge_csv_files(args.filenames, args.output_path)
