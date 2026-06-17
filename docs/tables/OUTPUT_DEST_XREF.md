# OUTPUT_DEST_XREF

> This table will be used by applications to store off default output destinations

**Description:** Output Destination Cross Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Id of the xrefed output destination |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the entity xrefed to this output dest entry |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the parent entity id xrefed |
| 4 | `PRINT_POINT_CD` | DOUBLE | NOT NULL |  | The PRINT_POINT_CD identifies if the packet is printed at order time, completion time, or only manually |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `USAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Device type code of the device which the output dest that is xref points to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |

