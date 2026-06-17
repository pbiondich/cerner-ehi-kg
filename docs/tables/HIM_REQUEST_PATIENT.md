# HIM_REQUEST_PATIENT

> This is a table that holds request information at patient level

**Description:** HIM REQUEST PATIENT  
**Table type:** ACTIVITY  
**Primary key:** `HIM_REQUEST_PATIENT_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPROVAL_IND` | DOUBLE |  |  | This is an indicator the is valued when a request needing approval is approved. |
| 6 | `AUTHORIZED_IND` | DOUBLE |  |  | Indicates if we have an authorization to fill this request |
| 7 | `AUTHORIZED_REJECT_REASON_CD` | DOUBLE | NOT NULL |  | This is the code value for the authorize reject reason |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who cancelled the request |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who created the request. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `HIM_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The primary key of him_request table |
| 14 | `HIM_REQUEST_PATIENT_ID` | DOUBLE | NOT NULL | PK | The primary key of this table |
| 15 | `LAST_UPDATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who last updated the request. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `REJECTED_REASON_CD` | DOUBLE | NOT NULL |  | This is the reason that the request was rejected |
| 18 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | This is the reason that the request was rejected |
| 19 | `REQUEST_STATUS_DT_TM` | DATETIME |  |  | This is the date and time that the status was set/changed |
| 20 | `REQUEST_STATUS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the person id of the person who is requesting this information |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CANCEL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HIM_REQUEST_ID` | [HIM_REQUEST](HIM_REQUEST.md) | `HIM_REQUEST_ID` |
| `LAST_UPDATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUEST_STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HIM_REQUEST_CRITERIA](HIM_REQUEST_CRITERIA.md) | `HIM_REQUEST_PATIENT_ID` |
| [HIM_RESTRICT_VIEW_HIST](HIM_RESTRICT_VIEW_HIST.md) | `HIM_REQUEST_PATIENT_ID` |

