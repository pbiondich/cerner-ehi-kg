# AP_TAG

> This reference table contains the individual specimen, block/cassette, and slide identification scheme values. For example, the values 1, 2, and 3 would be included on this table if a numeric scheme has been defined for association with a prefix.

**Description:** AP Tag  
**Table type:** REFERENCE  
**Primary key:** `TAG_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `TAG_DISP` | CHAR(7) |  |  | This field contains the tag display value. The display name is the value presented to the user viewing or ordering processing tasks. Tag display values of 1, 2, 3, etc., would be included (as separate tag values) for a numeric ID scheme. |
| 3 | `TAG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value (representing the identification scheme) that is associated with the individual tag value. Identification schemes are defined on the AP_TAG_GROUP reference table. |
| 4 | `TAG_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row (a single tag identification code value) in the AP_TAG table. |
| 5 | `TAG_SEQUENCE` | DOUBLE |  |  | This field contains the tag display sequence. The display sequence is used to organize the various tags associated with a single scheme. For example, the display sequence would dictate that 1 displays before 2 in a numeric scheme. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TAG_GROUP_ID` | [AP_TAG_GROUP](AP_TAG_GROUP.md) | `TAG_GROUP_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CASE_SPECIMEN](CASE_SPECIMEN.md) | `SPECIMEN_TAG_ID` |
| [CASSETTE](CASSETTE.md) | `CASSETTE_TAG_ID` |
| [SLIDE](SLIDE.md) | `TAG_ID` |

