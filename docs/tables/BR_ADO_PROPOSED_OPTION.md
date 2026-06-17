# BR_ADO_PROPOSED_OPTION

> Stores Advisor Orders Proposed Options for Topic, Scenario and Category.

**Description:** Bedrock Advisor Orders Proposed Option  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_PROPOSED_OPTION_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_PROPOSED_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The Detail that this option pertains to. Foreign Key to BR_ADO_PROP_DETAIL Table. |
| 2 | `BR_ADO_PROPOSED_OPTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_PROPOSED_OPTION table. |
| 3 | `NOTE_TXT` | VARCHAR(255) |  |  | Notes at Option Level |
| 4 | `OPTION_MEAN` | VARCHAR(50) | NOT NULL |  | Uniquely identifies the option from Readme/Content |
| 5 | `OPTION_SEQ` | DOUBLE | NOT NULL |  | Sequence assigned to Options within a Category |
| 6 | `PRESELECT_IND` | DOUBLE | NOT NULL |  | Indicates if this Option is to be set as a default. 1-Yes, 0-No |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_PROPOSED_DETAIL_ID` | [BR_ADO_PROPOSED_DETAIL](BR_ADO_PROPOSED_DETAIL.md) | `BR_ADO_PROPOSED_DETAIL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ADO_PROPOSED_ORD_LIST](BR_ADO_PROPOSED_ORD_LIST.md) | `BR_ADO_PROPOSED_OPTION_ID` |

