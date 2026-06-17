# SN_PREF_CARD_COMMENT

> Defines comment changes for an exception

**Description:** SugiNet Preference Card Exception Comment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME | NOT NULL |  | Date Time when the active ind was changed |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_PRSNL_ID` | DOUBLE |  | FK→ | user who activated the row |
| 4 | `COMMENT_TXT` | LONGTEXT |  |  | The text value for the comment being defined; |
| 5 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of comment being defined; |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date Time the comment was created; |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who created the comment for the preference card; |
| 8 | `SN_PREF_CARD_COMMENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | Preference Card the attribute is being defined for; |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |

