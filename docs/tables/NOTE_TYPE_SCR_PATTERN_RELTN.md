# NOTE_TYPE_SCR_PATTERN_RELTN

> It defines the relationships between tables NOTE_TYPE and SCR_PATTERN.

**Description:** Note Type and SCR Pattern Relationship table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NOTE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This serves as a foreign key to the NOTE_TYPE table. |
| 2 | `NOTE_TYPE_SCR_PATTERN_RELTN_ID` | DOUBLE | NOT NULL |  | Unique Identifier for this table |
| 3 | `SCR_PATTERN_CKI_IDENTIFIER` | VARCHAR(50) |  |  | External identifier for a pattern, used with SCR_PATTERN_CKI_SOURCE to form an external identifier. |
| 4 | `SCR_PATTERN_CKI_SOURCE` | CHAR(12) |  |  | External source for thiss pattern, used with SCR_PATTERN_CKI_ID to form an external identifier. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_TYPE_ID` | [NOTE_TYPE](NOTE_TYPE.md) | `NOTE_TYPE_ID` |

