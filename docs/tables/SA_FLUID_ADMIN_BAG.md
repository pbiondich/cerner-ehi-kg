# SA_FLUID_ADMIN_BAG

> Contains Bag information for given Fluid Admin

**Description:** SA Fluid Admin Bag  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BAG_VOLUME` | DOUBLE |  |  | The volume of the bag |
| 6 | `DONOR_IDENTIFIER` | VARCHAR(250) | NOT NULL |  | The identifier of the donor of the bag |
| 7 | `SA_FLUID_ADMIN_BAG_ID` | DOUBLE | NOT NULL |  | Unique identifier for the record |
| 8 | `SA_FLUID_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | The Fluid Admin the bag is associated to |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the bag |
| 10 | `START_DT_TM` | DATETIME | NOT NULL |  | The date/time the bag was started |
| 11 | `STOP_DT_TM` | DATETIME | NOT NULL |  | The date/time the bag was stopped |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_FLUID_ADMIN_ID` | [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `SA_FLUID_ADMIN_ID` |

