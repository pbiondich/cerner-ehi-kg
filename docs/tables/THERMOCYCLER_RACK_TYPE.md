# THERMOCYCLER_RACK_TYPE

> Defines the dimensions for thermocycler racks of a particular type.

**Description:** Thermocycler Rack Type  
**Table type:** REFERENCE  
**Primary key:** `RACK_TYPE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `RACK_TYPE_DESC` | VARCHAR(100) |  |  | The description of the Thermocycler Rack Type. Unique identifier the user gives the rack type. |
| 3 | `RACK_TYPE_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Thermocycler Rack Type record. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `X_ALPHA_IND` | DOUBLE |  |  | Indicates whether the horizontal coordinates of the Thermocycler Rack should be represented as characters. |
| 10 | `X_DIM` | DOUBLE |  |  | Horizontal dimension of the Thermocycler Rack. |
| 11 | `Y_ALPHA_IND` | DOUBLE |  |  | Indicates whether the vertical coordinates of the Thermocycler Rack should be represented as characters. |
| 12 | `Y_DIM` | DOUBLE |  |  | Vertical dimension of the Thermocycler Rack. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [THERMOCYCLER_RACK](THERMOCYCLER_RACK.md) | `RACK_TYPE_ID` |

