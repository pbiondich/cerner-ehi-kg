# RAD_EXAM

> Rad Exam

**Description:** Rad Exam  
**Table type:** ACTIVITY  
**Primary key:** `RAD_EXAM_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARGES_SENT_IND` | DOUBLE |  |  | This column indicates that technical charges have been sent to the AFC server. |
| 2 | `COMPLETE_DT_TM` | DATETIME |  |  | The Complete_Dt_Tm captures the date and time that the detail exam was performed. |
| 3 | `CREDIT_IND` | DOUBLE |  |  | The Credit_Ind indicates if the row represents bill only procedures that have been credited. |
| 4 | `EXAM_SEQUENCE` | DOUBLE |  |  | The Exam_Sequence defines the order in which the detail exams should appear or be performed. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Order_Radiology table. It identifies the order that the detail exams are a part of. |
| 6 | `QUANTITY` | DOUBLE |  |  | The Quantity field is used to capture the quantity of a specific bill only procedure that was used relative to the order. |
| 7 | `RAD_EXAM_ID` | DOUBLE | NOT NULL | PK | The Rad_Exam_Id uniquely identifies a row within the Rad_Exam table. This field serves no purpose other than to uniquely identify the row. |
| 8 | `REQUIRED_IND` | DOUBLE |  |  | The Required_Ind indicates whether or not the detail exam is required to complete. |
| 9 | `SCHED_REQ_DT_TM` | DATETIME |  |  | The Sched_Req_Dt_Tm contains the date that the detail exam was requested/scheduled to be performed on. |
| 10 | `SCHED_REQ_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The Service_Resource_Cd identifies the Exam Room that the detail exam is to be performed within. |
| 12 | `STARTING_DT_TM` | DATETIME |  |  | The Starting_Dt_Tm captures the date and time that the detail exam was started. |
| 13 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The Task_Assay_Cd is a foreign key to the Discrete_Task_Assay table. It identifies the detail examthat is to be performed. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_EXAM_PRSNL](RAD_EXAM_PRSNL.md) | `RAD_EXAM_ID` |
| [RAD_EXAM_PRSNL_HIST](RAD_EXAM_PRSNL_HIST.md) | `RAD_EXAM_ID` |

