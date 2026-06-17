# HCM_COMM_EVENT

> Stores communication information of patients/personnel

**Description:** Healthe Care Management Communication Event  
**Table type:** ACTIVITY  
**Primary key:** `HCM_COMM_EVENT_ID`  
**Columns:** 22  
**Referenced by:** 3 columns

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
| 12 | `HCM_COMM_EVENT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies communication information of patients/personnel. |
| 13 | `METHOD_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines the communication method for this row. |
| 14 | `MODIFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who modified the communication event. |
| 15 | `MODIFIED_DT_TM` | DATETIME |  |  | Indicates the date a communication event was modified. |
| 16 | `NOTES_CLOB` | LONGTEXT |  |  | Contains free text notes. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to which this communication is related. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTACTED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `CONTACTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MODIFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [HCM_COMM_EVENT_H](HCM_COMM_EVENT_H.md) | `HCM_COMM_EVENT_ID` |
| [HCM_COMM_EVENT_OUTCOME](HCM_COMM_EVENT_OUTCOME.md) | `HCM_COMM_EVENT_ID` |
| [HCM_COMM_EVENT_OUTCOME_H](HCM_COMM_EVENT_OUTCOME_H.md) | `HCM_COMM_EVENT_ID` |

