# MIC_REQUIRED_TASK

> This table contains the required tasks activity for an ordered procedure. When all required tasks are performed and verified for a procedure, it will be considered complete.

**Description:** Microbiology Required Tasks  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the antibiotic. Antibiotics are defined on code set 1011. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field is not used at this time |
| 3 | `COMPLETED_DT_TM` | DATETIME |  |  | This field identifies the date and time the orderable procedure was completed. |
| 4 | `COMPLETED_ID` | DOUBLE | NOT NULL |  | This field identifies the ID of the person who completed the procedure. The completed_id corresponds to the person_id on the prsnl table, which identifies the user. |
| 5 | `COMPLETION_IND` | DOUBLE |  |  | This field is not used at this time. |
| 6 | `DETAIL_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the detail susceptibility procedure. Detail susceptibility procedures are defined on code set 1004. |
| 7 | `DUE_DT_TM` | DATETIME |  |  | This field identifies the date and time the ordered task should have been completed. This field iscalculated upon insertion of the row based upon the tat_minutes and tat_units_cd. If the task comes from the reference data (at order time) then it uses the culture_start_dt_tm in the calculation. If the task is added to this table from Microbiology Result Entry, then the task_dt_tm is used in the |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 9 | `ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the organism associated with the required susceptibility task. Organisms are defined on code set 1021. |
| 10 | `ORGANISM_SEQ` | DOUBLE | NOT NULL |  | This field identifies a unique value for each organism code value entered. For example, if there are two GPC organisms associated with the orderable procedure the first GPC organism would have a sequence of 01 and the second GPC organism would have a sequence of 02. |
| 11 | `REQUIRED_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the current status of the report or susceptibility task. The status code_value is from code set 1901 Result Status. |
| 13 | `STATUS_FLAG` | DOUBLE |  |  | This field indicates the status of the report task. Valid values include: 0 = Database defined required report 1 = Performed report 2 = Database defined pending report |
| 14 | `TASK_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the task. This code value can come from several code sets depending on the type of task entered. Task related code sets include: 65 = Susceptibility Methods 1000 = Reports |
| 15 | `TASK_SEQ` | DOUBLE | NOT NULL |  | This field identifies a unique value for each required task assigned to an orderable procedure. |
| 16 | `TAT_MINUTES` | DOUBLE | NOT NULL |  | This field identifies the turnaround time defined for the report task and determines when the laboratory expects this report task to be completed. |
| 17 | `TAT_UNITS_CD` | DOUBLE | NOT NULL |  | This field identifies the time unit (i.e., minutes, hours, days) associated with the Tat_minutes. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANTIBIOTIC_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `DETAIL_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `ORDER_ID` | [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `ORDER_ID` |
| `ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `TASK_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

