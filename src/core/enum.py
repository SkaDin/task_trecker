from enum import StrEnum


class Status(StrEnum):
    NEW = "new"
    IN_PROCESS = "in_process"
    DONE = "done"
    OVERDUE = "overdue"


class Priority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
