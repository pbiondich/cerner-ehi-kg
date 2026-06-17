# PREGNANCY_ESTIMATE

> This table is used for recording the estimates of delivery date (and related information) for a pregnancy

**Description:** Pregnancy Estimate  
**Table type:** ACTIVITY  
**Primary key:** `PREGNANCY_ESTIMATE_ID`  
**Columns:** 26  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | ID which identifies the provider that recorded this estimate of delivery date. Value is from the PRSNL table. |
| 3 | `BIPARIETAL_DIAMETER` | DOUBLE |  |  | Measurement used in estimating gestational age (millimeters) |
| 4 | `CONFIRMATION_CD` | DOUBLE | NOT NULL |  | The confirmation level of the measurement of estimated delivery date. |
| 5 | `CROWN_RUMP_LENGTH` | DOUBLE |  |  | Measurement used in estimating gestational age (millimeters) |
| 6 | `DESCRIPTOR_CD` | DOUBLE | NOT NULL |  | Description of the advanced reproductive technology method |
| 7 | `DESCRIPTOR_FLAG` | DOUBLE | NOT NULL |  | Represents descriptive data pertaining to the method |
| 8 | `DESCRIPTOR_TXT` | VARCHAR(255) |  |  | Textual description relating to the method of estimation |
| 9 | `EDD_COMMENT_ID` | DOUBLE | NOT NULL |  | LONG_TEXT id that relates to a comment entered for the delivery date estimation |
| 10 | `ENTERED_DT_TM` | DATETIME |  |  | Date at which a user entered or altered a pregnancy estimate |
| 11 | `EST_DELIVERY_DT_TM` | DATETIME |  |  | Estimated delivery date |
| 12 | `EST_DELIVERY_TZ` | DOUBLE |  |  | Contains time zone information of EST_DELIVERY_DT_TM column |
| 13 | `EST_GEST_AGE_DAYS` | DOUBLE | NOT NULL |  | Estimated gestational age at time of measurement |
| 14 | `HEAD_CIRCUMFERENCE` | DOUBLE |  |  | Measurement used in estimating gestational age (millimeters) |
| 15 | `METHOD_CD` | DOUBLE | NOT NULL |  | The method by which the delivery date was determined |
| 16 | `METHOD_DT_TM` | DATETIME | NOT NULL |  | Date/time that the method of estimation occurred (for example, ultrasound date) |
| 17 | `METHOD_TZ` | DOUBLE |  |  | Contains time zone information of METHOD_DT_TM column |
| 18 | `PREGNANCY_ESTIMATE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 19 | `PREGNANCY_ID` | DOUBLE | NOT NULL | FK→ | The pregnancy to which this delivery date estimate is related |
| 20 | `PREV_PREG_ESTIMATE_ID` | DOUBLE | NOT NULL | FK→ | PREVIOUS PRENANCY EST ID OF GROUP |
| 21 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates finality of the estimate |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PREGNANCY_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |
| `PREV_PREG_ESTIMATE_ID` | [PREGNANCY_ESTIMATE](PREGNANCY_ESTIMATE.md) | `PREGNANCY_ESTIMATE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PREGNANCY_DETAIL](PREGNANCY_DETAIL.md) | `PREGNANCY_ESTIMATE_ID` |
| [PREGNANCY_ESTIMATE](PREGNANCY_ESTIMATE.md) | `PREV_PREG_ESTIMATE_ID` |

