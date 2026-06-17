# HCM_COMM_EVENT_H

> Stores communication information of patients/personnel

**Description:** Healthe Care Management Communication Event History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMM_DT_TM` | DATETIME | NOT NULL |  | The documented communication event date and time for the row. |
| 3 | `COMM_PERSON_ROLE_CD` | DOUBLE | NOT NULL |  | This column contains the code that defines the communication person role for the row. |
| 4 | `COMM_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines the communication type for the row. |
| 5 | `CONTACTED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel contacted. |
| 6 | `CONTACTED_PERSON_NAME` | VARCHAR(255) | NOT NULL |  | The free text name of the person contacted for the row. |
| 7 | `CONTACTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel making the contact. |
| 8 | `CREATED_BY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person that created the row on the table. |
| 9 | `CREATED_DT_TM` | DATETIME |  |  | Indicates the date a communication event was created. |
| 10 | `DURATION_IN_MIN` | DOUBLE |  |  | The duration of the contact in minutes. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter |
| 12 | `HCM_COMM_EVENT_H_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a historical record related to a communication event. |
| 13 | `HCM_COMM_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies communication information of patients/personnel. |
| 14 | `METHOD_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines the communication method for this row. |
| 15 | `MODIFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who modified the communication event. |
| 16 | `MODIFIED_DT_TM` | DATETIME |  |  | Indicates the date a communication event was modified. |
| 17 | `NOTES_CLOB` | LONGTEXT |  |  | Contains free text notes. |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to which this communication is related. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTACTED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `CONTACTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HCM_COMM_EVENT_ID` | [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `HCM_COMM_EVENT_ID` |
| `MODIFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

