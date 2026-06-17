# BR_SETUP_WIZARD_LOC_RELTN

> Stores relationships between locations and setup wizards.

**Description:** Bedrock Setup Wizard Location Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_SETUP_WIZARD_ID` | DOUBLE | NOT NULL | FK→ | Identifies the wizard associated with this location. |
| 2 | `BR_SETUP_WIZARD_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_SETUP_WIZARD_LOC_RELTN table. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies the location associated to this setup wizard. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_SETUP_WIZARD_ID` | [BR_SETUP_WIZARD](BR_SETUP_WIZARD.md) | `BR_SETUP_WIZARD_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

