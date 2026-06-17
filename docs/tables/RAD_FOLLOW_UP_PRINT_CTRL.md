# RAD_FOLLOW_UP_PRINT_CTRL

> RadNet Mammography letter printer control

**Description:** Radiology Follow Up Print Control  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEPARTMENT_CD` | DOUBLE |  | FK→ | Department code for which printer is assigned |
| 2 | `FOLLOW_UP_CONTROL_ID` | DOUBLE |  | FK→ | This serves as a foreign key to the Rad_Follow_Up_Control table. It uniquely identifies the follow-up system control that the printer control is a part of. |
| 3 | `FOLLOW_UP_DEFAULT_TYPE_CD` | DOUBLE |  |  | Identifies the type of follow-up letter that is involved. |
| 4 | `FOLLOW_UP_PRINT_CTRL_ID` | DOUBLE | NOT NULL |  | The Follow_Up_Print_Ctrl_Id serves as a primary key for the rad_follow_up_print_ctrl table. It serves no other purpose other than to uniquely identify the row. |
| 5 | `SECTION_CD` | DOUBLE |  | FK→ | Section code for which printer is assigned |
| 6 | `SEQUENCE` | DOUBLE |  |  | Letter sequence that corresponds to Sequence on Rad_Follow_Up_Default. It identifies the order in which the letters should be sent. |
| 7 | `SUBSECTION_CD` | DOUBLE |  | FK→ | The Subsection code for which the printer is assigned |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEPARTMENT_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `FOLLOW_UP_CONTROL_ID` | [RAD_FOLLOW_UP_CONTROL](RAD_FOLLOW_UP_CONTROL.md) | `FOLLOW_UP_CONTROL_ID` |
| `SECTION_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SUBSECTION_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

