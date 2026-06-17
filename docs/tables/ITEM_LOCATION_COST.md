# ITEM_LOCATION_COST

> Contains an items cost at a location per package type.

**Description:** Item Location Cost  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST` | DOUBLE | NOT NULL |  | This cost of the item. |
| 2 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The cost type code allows differentiation between average cost, current cost, last cost, etc. |
| 3 | `COST_UPLOAD_IND` | DOUBLE | NOT NULL |  | Indicates whether this organization's average/last cost was created through cost upload or not. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 7 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 8 | `INITIAL_ORG_COST_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether the item's cost is initial org cost calculated by system. In other way, if this ind is set to 0, then it means that the item has transactions associated for the item at this location. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to item_definition table. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 11 | `MANUAL_ORG_COST_AMT` | DOUBLE | NOT NULL |  | The Organization cost which is updated/inserted manually through mmdbtool.exe or uploadmanager or interface. |
| 12 | `MANUAL_ORG_COST_UPDT_IND` | DOUBLE | NOT NULL |  | Indicates whether the cost is updated manually (through mmdbtool.exe or uploadmanager or interface) or automatically. |
| 13 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | Foreign key to package_type table |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

