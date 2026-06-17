# SN_PREF_CARD_EXCEPTION

> Defines what exceptions exist for a Preference Card

**Description:** SugiNet Preference Card Exception  
**Table type:** REFERENCE  
**Primary key:** `SN_PREF_CARD_EXCEPTION_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME | NOT NULL |  | Date and Time the exception was made active or inactive; |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_PRSNL_ID` | DOUBLE |  | FK→ | user who activated the row |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and Time the exception was created; |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who created the exception; |
| 6 | `EXCEPTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines what the exception is tied to (ex. Surgeon, Specialty, etc.); |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Table PK the exception applies to; |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Table Name the exception applies to; |
| 9 | `SN_PREF_CARD_EXCEPTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 10 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | Preference Card the exception is for; |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SN_PREF_CARD_EXCEPT_ADD](SN_PREF_CARD_EXCEPT_ADD.md) | `SN_PREF_CARD_EXCEPTION_ID` |
| [SN_PREF_CARD_EXCEPT_COMMENT](SN_PREF_CARD_EXCEPT_COMMENT.md) | `SN_PREF_CARD_EXCEPTION_ID` |
| [SN_PREF_CARD_EXCEPT_REMOVE](SN_PREF_CARD_EXCEPT_REMOVE.md) | `SN_PREF_CARD_EXCEPTION_ID` |

