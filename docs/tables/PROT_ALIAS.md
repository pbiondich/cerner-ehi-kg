# PROT_ALIAS

> This table contains the aliases for a protocol

**Description:** PROT ALIAS  
**Table type:** REFERENCE  
**Primary key:** `PROT_ALIAS_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_ID` | DOUBLE | NOT NULL | FK→ | A unique key for the Protocol alias on a protocol. No two active rows can have the same Alias_id. |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Identifies the alias pool to which this protocol alias belongs |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PROT_ALIAS` | VARCHAR(255) | NOT NULL |  | This field contains the protocol mnemonic/code assigned to the protocol by an institution associated with the protocol. |
| 6 | `PROT_ALIAS_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prot_alias table. It is an internal system assigned number. |
| 7 | `PROT_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the code for the type of alias this protocol alias represents. |
| 8 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_master table. This field identifies the protocol for which this protocol alias applies |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_ID` | [PROT_ALIAS](PROT_ALIAS.md) | `PROT_ALIAS_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROT_ALIAS](PROT_ALIAS.md) | `ALIAS_ID` |

