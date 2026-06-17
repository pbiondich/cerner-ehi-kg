# TUBE_INFORMATION

> Additional information about an HLA molecular testing primer kit tube.

**Description:** Tube Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relates the Aliquotted Primer Kit tube information to the inventory lot and related map. It is a foreign key reference to the primary key of the lot_number_info table. |
| 2 | `TUBE_DESC` | VARCHAR(255) |  |  | Additional information about a specific tube in an aliquotted primer kit. |
| 3 | `TUBE_NUMBER` | DOUBLE | NOT NULL |  | Number of the aliquotted primer kit tube. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [ALIQUOTTED_PRIMER_KIT](ALIQUOTTED_PRIMER_KIT.md) | `LOT_NUMBER_ID` |

