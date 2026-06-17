# RXS_LOC_ATTR

> Stores the attributes to fully describe a RxStation location's type, behavior and configuration.

**Description:** RxStation Location Attribute  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTR_CD` | DOUBLE | NOT NULL |  | The attribute of the RxStation being defined. Examples are: humidity control (for a device level location) , mobility (for a tray level - whether the tray is fixed like a shelf or can be pulled out) |
| 2 | `ATTR_VALUE_TXT` | VARCHAR(1000) | NOT NULL |  | The value appropriate for a particular attribute of a particular RxStation device. |
| 3 | `LOC_CD` | DOUBLE | NOT NULL | FK→ | The representation of the RxStation device or components in the Location model. |
| 4 | `RXS_LOC_ATTR_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a row in the RXS_LOC_ATTR table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

