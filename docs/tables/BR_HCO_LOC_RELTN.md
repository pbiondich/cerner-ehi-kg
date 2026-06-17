# BR_HCO_LOC_RELTN

> Stores locations associated with an HCO Number.

**Description:** Bedrock Health Care Organization Location Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | The HCO related to this location. |
| 2 | `BR_HCO_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_HCO_LOC_RELTN table. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location associated with this Healthcare Organization. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_HCO_ID` | [BR_HCO](BR_HCO.md) | `BR_HCO_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

