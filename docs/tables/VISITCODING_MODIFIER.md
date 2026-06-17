# VISITCODING_MODIFIER

> Stores lists of modifiers associated to an E&M code in the visitcoding_audit table

**Description:** Visit Coding Modifier  
**Table type:** ACTIVITY  
**Primary key:** `VISITCODING_MODIFIER_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODIFIER_CD` | DOUBLE | NOT NULL |  | Modifier Code |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Key to the visitcoding_audit record containing the modified E&M code. |
| 8 | `VISITCODING_MODIFIER_ID` | DOUBLE | NOT NULL | PK | Primary id |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VISITCODING_AUDIT_ID` | [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODING_AUDIT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [VISITCODING_BILLITEM](VISITCODING_BILLITEM.md) | `VISITCODING_MODIFIER_ID` |

