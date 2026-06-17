# TAG_FOUNDATION

> This reference table contains Cerner-provided starter data that can be used to create identification schemes which can be associated with specimen, block/cassette, and slides. This starter table contains individual identification code values.

**Description:** Tag Foundation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TAG_DISPLAY` | CHAR(7) |  |  | This field contains the individual tag display value. For example, individual tag values associated with a numeric grouping might include 1, 2 and 3. |
| 2 | `TAG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value (representing the tag grouping) used to join to information stored on the TAG_GROUP_FOUNDATION reference table. |
| 3 | `TAG_SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a sequence documenting the individual tag value's location in the group scheme. The tag associated with the lowest sequence number displays first; the tag with the highest sequence number displays last. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TAG_GROUP_ID` | [TAG_GROUP_FOUNDATION](TAG_GROUP_FOUNDATION.md) | `TAG_GROUP_ID` |

