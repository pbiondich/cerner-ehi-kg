# MED_ADMIN_IDENT_ERROR

> Medical Administration Identification Errors Table

**Description:** Medical Administration Identification Errors  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of error recorded |
| 2 | `BAR_CODE_IDENT` | VARCHAR(50) | NOT NULL |  | The bar code identifier that was scanned. |
| 3 | `CAREAWARE_USED_IND` | DOUBLE | NOT NULL |  | Maintains whether CareAware was used to obtain drug related information. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the patient Encounter, if known, associated to this identification error event. |
| 5 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | The date/time that the identification error occurred. |
| 6 | `MED_ADMIN_IDENT_ERROR_ID` | DOUBLE | NOT NULL |  | The ID of the identification error event. |
| 7 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit of the device the user is using when the identification error happened. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the user associated to this identification error event. |
| 9 | `SOURCE_APPLICATION_FLAG` | DOUBLE |  |  | Identification for source application used to chart med event. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

