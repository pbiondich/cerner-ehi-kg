# BR_CAT_EVENT_NORMALCY

> Stores related Event Code and Normalcy Code information, used in Multiple Drug Resistance Organisms (MDRO) Bedrock Wizard.

**Description:** Bedrock Multiple Drug Resistance Organism Category Event Normalcy  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CAT_EVENT_NORMALCY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_CAT_EVENT_NORMALCY table. |
| 2 | `BR_MDRO_CAT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The event that this normalcy code is related to. |
| 3 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | "CODE SET: 52 Stores Code value of the Normalcy Codes associated with this Event Code." |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_MDRO_CAT_EVENT_ID` | [BR_MDRO_CAT_EVENT](BR_MDRO_CAT_EVENT.md) | `BR_MDRO_CAT_EVENT_ID` |

