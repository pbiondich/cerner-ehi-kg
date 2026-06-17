# GL_ALIAS_FIELD_RESULT

> An alias for the General Ledger Field Result

**Description:** General Ledger Alias Field Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 7 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | FK to the person table |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `GL_ALIAS_FIELD_RELTN_ID` | DOUBLE | NOT NULL | FK→ | FK to the gl_alias_field_reltn table |
| 10 | `GL_ALIAS_FIELD_RESULT_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 11 | `GL_FIELD_ALIAS_CODE` | VARCHAR(200) | NOT NULL |  | CDM code value that is entered by the user. |
| 12 | `GL_FIELD_VALUE` | DOUBLE |  |  | General Ledger Field Value |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `GL_ALIAS_FIELD_RELTN_ID` | [GL_ALIAS_FIELD_RELTN](GL_ALIAS_FIELD_RELTN.md) | `GL_ALIAS_FIELD_RELTN_ID` |

