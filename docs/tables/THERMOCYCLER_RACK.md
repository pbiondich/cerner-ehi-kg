# THERMOCYCLER_RACK

> Defines a unique name for a thermocycler rack and the type of the rack.

**Description:** Thermocycler Rack  
**Table type:** REFERENCE  
**Primary key:** `RACK_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `RACK_DESC` | VARCHAR(20) |  |  | The description of the Thermocycler Rack. Unique identifier the user gives the rack. |
| 3 | `RACK_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Thermocycler Rack record. |
| 4 | `RACK_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the rack type of the thermocycler rack. It is a foreign key reference to the primary key of the themocycler_rack_type table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RACK_TYPE_ID` | [THERMOCYCLER_RACK_TYPE](THERMOCYCLER_RACK_TYPE.md) | `RACK_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [GEL_BATCH](GEL_BATCH.md) | `RACK_ID` |

