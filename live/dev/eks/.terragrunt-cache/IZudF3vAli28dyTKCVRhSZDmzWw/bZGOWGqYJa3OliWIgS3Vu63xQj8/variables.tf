variable "vpc_id" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
}

variable "admin_arn" {
  type = string
}