# MFA_METHOD_CHAIN

> Stores the Methods associated with a Mode, and the sequence in which the Mode Methods will be processed

**Description:** MFA Method Chain  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAIN_SEQUENCE` | DOUBLE | NOT NULL |  | Position of this entry in the mode's list of methods |
| 2 | `MFA_METHOD_CHAIN_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `MFA_METHOD_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Method table. |
| 4 | `MFA_MODE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the MODE table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MFA_METHOD_ID` | [MFA_METHOD](MFA_METHOD.md) | `MFA_METHOD_ID` |
| `MFA_MODE_ID` | [MFA_MODE](MFA_MODE.md) | `MFA_MODE_ID` |

