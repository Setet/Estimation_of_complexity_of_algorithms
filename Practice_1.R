# 1.Скалярное умножение векторов
skal_mult <- function(x, y, al) {
  len_vec <- c()
  result = 0
  for (i in 1:length(x)) {
    len_vec[i] <- sqrt(x[i] ^ 2 + y[i] ^ 2)
  }
  #View(len_vec)
  
  result = len_vec[1] * len_vec[2] * cos(al)
  return(result)
}

# 1
x <- c(5, 2)
y <- c(4, 2)
al = runif(1, min = 0, max = pi)

summ_skal <- skal_mult(x, y, al)
#View(summ_skal)

# 2.Перемножение матриц
n = 4
A <- matrix(runif(n * n, min = -50, max = 50), nrow = n, ncol = n)

B <- matrix(runif(n * n, min = -50, max = 50), nrow = n, ncol = n)

C <- matrix(0, nrow = n, ncol = n)

for (i in 1:n) {
  for (j in 1:n) {
    for (k in 1:n) {
      C[i, j] = C[i, j] + A[i, k] * B[k, j]
    }
  }
}

# 3.Сортировки массивов
# Пузырьковая сортировка
# T_max(n)=4*((n-1)*(n/2)) | T_max(10)=4*(9*5)=135
# T_min(n)=1*((n-1)*(n/2)) | T_min(10)=45
# T_mean(n)=???
bubble_sort <- function(x)
{
  k_bubble_sort = 0
  n <- length(x)
  for (i in 1:(n - 1)) {
    for (j in 1:(n - i)) {
      if (x[j] > x[j + 1]) {
        temp <- x[j]
        x[j] <- x[j + 1]
        x[j + 1] <- temp
        k_bubble_sort = k_bubble_sort + 4
      }
    }
  }
  View(k_bubble_sort)
  x
}

# Сортировка вставками
# T_max(n)=2*(n*((n-1)/2)) | T_max(10)=2*(10*((10-1)/2))=45
# T_min(n)=1*(n*((n-1)/2))
# T_mean(n)=???
insertion_sort <- function(x)
{
  k_insertion_sort = 0
  n <- length(x)
  for (i in 2:(n))
  {
    key = x[i]
    j   = i - 1
    while (j > 0 && x[j] > key)
    {
      x[j + 1] = x[j]
      j = j - 1
      k_insertion_sort = k_insertion_sort + 2
    }
    x[j + 1] = key
  }
  View(k_insertion_sort)
  x
}

# Сортировка выборкой
# T_max(n)=N^2+2n-3
# T_min(n)=(1/2n+3)(n-1)
# T_mean(n)=???
selection_sort <- function(x)
{
  k_selection_sort = 0
  n <- length(x)
  for (i in 1:(n - 1))
  {
    min_index <- i
    for (j in (i + 1):(n))
    {
      if (x[j] < x[min_index]) {
        min_index = j
        k_selection_sort = k_selection_sort + 1
      }
    }
    temp <- x[i]
    x[i] <- x[min_index]
    x[min_index] <- temp
    k_selection_sort = k_selection_sort + 3
  }
  View(k_selection_sort)
  x
}

arr <- c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print("Начальный массив :")
print(arr)
print("Пузырьковая сортировка :")
print(bubble_sort(arr))
print("Сортировка вставками :")
print(insertion_sort(arr))
print("Сортировка выборкой :")
print(selection_sort(arr))