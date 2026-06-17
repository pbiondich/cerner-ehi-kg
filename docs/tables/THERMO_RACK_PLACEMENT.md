# THERMO_RACK_PLACEMENT

> Specifies the placement of alliquotted HLA molecular primer kit tubes on a thermocycler rack for an order.

**Description:** Thermocycler Rack Placement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_ID` | DOUBLE | NOT NULL |  | Relates the placed aliquotted primer kit tube to a gel batch. It is a foreign key reference to the primary key of the gel_batch table. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the aliquotted primer kit the tube which was placed came from. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL |  | Relates the placed aliquotted primer kit tube to an order. It is a foreign key reference to the primary key of the orders table. |
| 4 | `RACK_ID` | DOUBLE | NOT NULL |  | Identifies the thermocycler rack which is being populated by aliquotted primer kit tubes. |
| 5 | `TUBE_NUMBER` | DOUBLE |  |  | Number of the aliquotted primer kit tube which was placed on the thermocycler rack at this position. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `X_POS` | DOUBLE | NOT NULL |  | Horizontal coordinate where the aliquotted primer kit tube was placed. |
| 12 | `Y_POS` | DOUBLE | NOT NULL |  | Vertical coordinate where the aliquotted primer kit tube was placed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [ALIQUOTTED_PRIMER_KIT](ALIQUOTTED_PRIMER_KIT.md) | `LOT_NUMBER_ID` |

