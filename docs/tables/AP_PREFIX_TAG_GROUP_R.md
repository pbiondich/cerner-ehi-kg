# AP_PREFIX_TAG_GROUP_R

> This reference table contains the identification scheme assigned to the prefix and the tag type. The tag type options include specimen, block (cassette), and slide. Each prefix and tag type scheme is included as a unique entry on this table.

**Description:** AP Prefix Tag Group Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the prefix to which the identification scheme for specimens, blocks/cassettes, or slides is associated. This field contains the foreign key value used to join to the prefix information stored on the AP_PREFIX table. |
| 2 | `PRIMARY_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not the tag scheme is the primary (default) specimen tag scheme. |
| 3 | `TAG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value (representing the identification scheme associated with the prefix) used to join to the scheme information stored on the AP_TAG_GROUP reference table. |
| 4 | `TAG_SEPARATOR` | CHAR(1) |  |  | This field contains the tag separator value associated with the prefix, tag type (block or slide), and tag group (identification scheme). Tag separator values are optional, and are used to separate, visually, one ID element from another. |
| 5 | `TAG_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field contains a flag value indicating which tag type (specimen, block/cassette, or slide) is associated with the prefix and identification scheme. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `TAG_GROUP_ID` | [AP_TAG_GROUP](AP_TAG_GROUP.md) | `TAG_GROUP_ID` |

