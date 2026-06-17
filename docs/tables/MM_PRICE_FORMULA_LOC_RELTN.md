# MM_PRICE_FORMULA_LOC_RELTN

> Links the price schedules with locations. This will only be populated if the organization is not tracking costs at the organization level.

**Description:** Pricing Formula Location Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location that this pricing formula is associated with. |
| 2 | `LOC_SEQ` | DOUBLE | NOT NULL |  | The order the locations are to be applied for a particular formula. |
| 3 | `MM_PRICE_FORMULA_ID` | DOUBLE | NOT NULL | FK→ | The formula for which this location applies. |
| 4 | `MM_PRICE_FORMULA_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_PRICE_FORMULA_LOC_RELTN table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `MM_PRICE_FORMULA_ID` | [MM_PRICE_FORMULA](MM_PRICE_FORMULA.md) | `MM_PRICE_FORMULA_ID` |

