from xlrd import open_workbook


class ReadExcel(object):
    # 封装读取Excel数据的方法

    @staticmethod
    def open_excel(file_path, sheet_name):
        # 文件路径、工作薄名称

        open_excel_file = open_workbook(file_path)
        # 打开Excel文件
        get_sheet = open_excel_file.sheet_by_name(sheet_name)
        # 获取工作表
        row_number = get_sheet.nrows
        # 获取行数
        data_list = []
        # 数据List
        for i in range(1, row_number):
            # 从第二行开始遍历每一行
            data_list.append(get_sheet.row_values(i))
            # 把每个单元格的数值存放到dataList中
        print(data_list)
        return data_list


