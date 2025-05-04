def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    max_lines = max(len(lines1), len(lines2))
    
    print(f"Perbandingan antara {file1} dan {file2}:\n")
    print("{:<10} {:<50} {:<50}".format("Baris", file1, file2))
    print("-" * 110)
    
    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else "(tidak ada)"
        line2 = lines2[i].strip() if i < len(lines2) else "(tidak ada)"
        
        if line1 != line2:
            print("{:<10} {:<50} {:<50}".format(i+1, line1, line2))

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")
compare_files(file1, file2)