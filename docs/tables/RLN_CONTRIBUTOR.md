# RLN_CONTRIBUTOR

> This table will store the relationship between a partner lab organization and a contributor source, along with associated sub-activity type, order suffix and assay suffix.

**Description:** Reference Lab Network - Contributor  
**Table type:** REFERENCE  
**Primary key:** `RLN_CONTRIBUTOR_ID`  
**Columns:** 16  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the sub activity type for this contributor. |
| 4 | `ASSAY_SUFFIX_TXT` | VARCHAR(40) |  |  | Contains the assay suffix. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related contributor source. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `ORDER_SUFFIX_TXT` | VARCHAR(40) |  |  | Contains the suffix for the order. |
| 9 | `ORIG_RLN_CONTRIBUTOR_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the contribution information. This field will always point back to the original value created. This may be used to find the correct version when combined with the begin and end effective dates and times. |
| 10 | `PARTNER_ORG_IDENT` | DOUBLE | NOT NULL |  | Uniquely identifies an RLN partner lab organization. This identifier comes from the RLN Cloud database. |
| 11 | `RLN_CONTRIBUTOR_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the related contributor. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORIG_RLN_CONTRIBUTOR_ID` | [RLN_CONTRIBUTOR](RLN_CONTRIBUTOR.md) | `RLN_CONTRIBUTOR_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RLN_BENCH](RLN_BENCH.md) | `RLN_CONTRIBUTOR_ID` |
| [RLN_COMPONENT_MAP](RLN_COMPONENT_MAP.md) | `RLN_CONTRIBUTOR_ID` |
| [RLN_CONTRIBUTOR](RLN_CONTRIBUTOR.md) | `ORIG_RLN_CONTRIBUTOR_ID` |
| [RLN_SPECIMEN_OEF](RLN_SPECIMEN_OEF.md) | `RLN_CONTRIBUTOR_ID` |

