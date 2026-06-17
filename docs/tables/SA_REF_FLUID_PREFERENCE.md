# SA_REF_FLUID_PREFERENCE

> This table will store the default units of measure and various display options to be used for a fluids in the anesthesia fluids dialog

**Description:** Anethesia reference fluid preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEF_ROUTE_CD` | DOUBLE | NOT NULL |  | Stores the default route for a Fluid. |
| 3 | `INFUSION_DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines what to display for fluids |
| 4 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Doc Type Preference Set is tied to |
| 5 | `SA_REF_FLUID_ID` | DOUBLE | NOT NULL | FK→ | Unique value to the fluid item record |
| 6 | `SA_REF_FLUID_PREFERENCE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the sa_ref_fluid_preference table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VOLUME_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of volume |
| 13 | `VOLUME_RATE_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of concentration |
| 14 | `VOLUME_RATE_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time field of concentration |
| 15 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in WBD |
| 16 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in WBD |
| 17 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_DOC_TYPE_ID` | [SA_REF_DOC_TYPE](SA_REF_DOC_TYPE.md) | `SA_REF_DOC_TYPE_ID` |
| `SA_REF_FLUID_ID` | [SA_REF_FLUID](SA_REF_FLUID.md) | `SA_REF_FLUID_ID` |

