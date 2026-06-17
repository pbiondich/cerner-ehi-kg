# PC_ATTRIBUTE_VALUE

> This table is a reference table for all PC attributes' values. It will hold the values for the attributes of a particular PC defined in the Millennium system.

**Description:** PC Attribute Value  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_ID` | DOUBLE | NOT NULL | FK→ | Unique number identifying the PC attributes (PC_ATTRIBUTE) |
| 2 | `ATTRIBUTE_VALUE_ID` | DOUBLE | NOT NULL |  | Primary Key; Unique number identifying the PC attribute value |
| 3 | `ATTRIBUTE_VALUE_OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | The PC attribute output destination code value; Unique number identifying an output destination (OUTPUT_DEST) |
| 4 | `ATTRIBUTE_VALUE_TXT` | VARCHAR(100) | NOT NULL |  | The PC attribute textual value |
| 5 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Unique number identifying the PC device (DEVICE) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTRIBUTE_ID` | [PC_ATTRIBUTE](PC_ATTRIBUTE.md) | `ATTRIBUTE_ID` |
| `ATTRIBUTE_VALUE_OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `DEVICE_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |

