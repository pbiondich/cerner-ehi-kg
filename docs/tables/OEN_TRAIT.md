# OEN_TRAIT

> Holds all the possible interface traits.

**Description:** oen_trait  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOMAIN_NBR` | DOUBLE | NOT NULL |  | Defines which domain the trait belongs in. |
| 3 | `FORMAT_LIST` | VARCHAR(30) |  |  | Defines which formats this trait applies to. |
| 4 | `HIDDEN_IND` | DOUBLE |  |  | Should this trait be hidden |
| 5 | `LIST_IND` | DOUBLE |  |  | Is this trait a list? |
| 6 | `PROD_CHG_IND` | DOUBLE |  |  | Can this trait be changed while the interface is in production? |
| 7 | `PROTOCOL_LIST` | VARCHAR(30) |  |  | List of protocols this trait applies to. |
| 8 | `SERVICE_LIST` | VARCHAR(30) |  |  | Which services does this trait apply to |
| 9 | `TRAIT_DESC` | VARCHAR(255) |  |  | Description |
| 10 | `TRAIT_ID` | DOUBLE | NOT NULL |  | Id of the Trait |
| 11 | `TRAIT_NAME` | VARCHAR(32) | NOT NULL |  | Name of trait |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALUE_TYPE` | DOUBLE |  |  | What type of value will this trait hold. |
| 18 | `VERSIONING_IND` | DOUBLE |  |  | Should this trait be versioned. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

