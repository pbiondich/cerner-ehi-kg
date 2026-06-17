# BENEFIT_DETAIL

> Deifnes details for a plan benefit, including quantity and scope of coverage

**Description:** Defines details for a plan benefit, including quantity and scope of coverage  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique, system-generated identifier for the benefit detail record. |
| 7 | `BENEFIT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the benefit which this detail record describes. |
| 8 | `BNFT_EVENT_CD` | DOUBLE | NOT NULL |  | Defines the type of event described in the detail record. |
| 9 | `BNFT_EVENT_QTY` | DOUBLE |  |  | The number of benefits of this type that will be covered/excluded under the benefits of the plan |
| 10 | `BNFT_SCOPE_CD` | DOUBLE | NOT NULL |  | Defines the scope of coverage for the defined benefit event |
| 11 | `BNFT_SCOPE_VAL` | DOUBLE |  |  | The value that describes the magnitude of the scope of coverage. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `FT_BNFT_EVENT` | VARCHAR(50) |  |  | Text field for describing a benefit detail that cannot be defined by codes; must use the "OTHER" meaning in the bnft_event_cd field in conjunction with this field. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_ID` | [BENEFIT](BENEFIT.md) | `BENEFIT_ID` |

