# AMENDMENT_ALIAS

> This table is used to store the aliases for an amendment

**Description:** AMENDMENT ALIAS  
**Table type:** REFERENCE  
**Primary key:** `AMENDMENT_ALIAS_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_ID` | DOUBLE | NOT NULL | FK→ | A unique key for the Amendment alias on a protocol. No two active rows can have the same Alias_id. |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Identifies the alias pool to which this alias belongs |
| 3 | `AMENDMENT_ALIAS` | VARCHAR(255) | NOT NULL |  | This is the alias assigned to the amendment |
| 4 | `AMENDMENT_ALIAS_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the amendment_alias table. It is an internal system assigned number. |
| 5 | `AMENDMENT_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Protocol Alias Type |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the prot_amendment table. It is an internal system assigned number. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_ID` | [AMENDMENT_ALIAS](AMENDMENT_ALIAS.md) | `AMENDMENT_ALIAS_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AMENDMENT_ALIAS](AMENDMENT_ALIAS.md) | `ALIAS_ID` |

