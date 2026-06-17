# EKS_MODULE_AUDIT

> Used by eks servers to log the results of having run a module.

**Description:** eks server module audit table  
**Table type:** ACTIVITY  
**Primary key:** `REC_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_COUNT` | DOUBLE |  |  | Count of action template results. |
| 2 | `ACTION_EXEC_SECS` | DOUBLE |  |  | Will contain how long in seconds, the action section of the rule execution took to complete. |
| 3 | `ACTION_RETURN` | CHAR(100) |  |  | Action return values as an array of 3 digit numbers. |
| 4 | `BEGIN_DT_TM` | DATETIME |  |  | The date/time the module began. |
| 5 | `CONCLUDE` | DOUBLE |  |  | Module's overall conclusion result. 0 - logic false, 1-logic true, 2-action(s) performed. |
| 6 | `END_DT_TM` | DATETIME |  |  | The date/time the module ended. |
| 7 | `EVENT_NUMBER` | DOUBLE |  |  | EKS Internal event number that triggered this module. |
| 8 | `LOGIC_COUNT` | DOUBLE |  |  | Count of templates returning a value in the logic section. |
| 9 | `LOGIC_EXEC_SECS` | DOUBLE |  |  | Will contain how long in seconds, the logic section of the rule execution took to complete. |
| 10 | `LOGIC_RETURN` | CHAR(100) |  |  | Array of 3 digit values denoting the return values for templates in the logic section. |
| 11 | `MODULE_NAME` | CHAR(30) |  |  | Name of the module that ran in the server. |
| 12 | `MODULE_VERSION` | VARCHAR(10) |  |  | Current Module Version executed for the rule instance. |
| 13 | `PERSONNEL_ID` | DOUBLE | NOT NULL |  | Personnel ID of the person that initiated module firing by performing system request. ***Obsolete column. Column never populated. Always 0.*** |
| 14 | `REC_ID` | DOUBLE | NOT NULL | PK | Contains the record sequence obtained from eks_module_audit_seq when inserting into table. Contains a unique key from a sequence. |
| 15 | `REQUEST_NUMBER` | DOUBLE |  |  | System request number that triggered EKS internal event. |
| 16 | `SERVER_CLASS` | CHAR(40) |  |  | The class of the server that ran the module. |
| 17 | `SERVER_INSTANCE` | DOUBLE |  |  | The CSA instance number of the server that ran the module. |
| 18 | `SERVER_NODE` | VARCHAR(30) |  |  | Linux/AIX application node name the server instance is running on. |
| 19 | `SERVER_NUMBER` | DOUBLE |  |  | The number of the server that ran the module (domain + directory entry number). |
| 20 | `SERVER_RTLLOG` | VARCHAR(30) |  |  | The server rtl log name written in $CCLUSERDIR. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EKS_MODULE_AUDIT_DET](EKS_MODULE_AUDIT_DET.md) | `MODULE_AUDIT_ID` |

