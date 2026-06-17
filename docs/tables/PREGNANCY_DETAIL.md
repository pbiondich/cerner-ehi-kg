# PREGNANCY_DETAIL

> This table is used for recording additional details which may pertain to some pregnancy estimates

**Description:** Pregnancy DetailT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BREASTFEEDING_IND` | DOUBLE | NOT NULL |  | Indicates whether the person was already breastfeeding at time of conception |
| 4 | `CONTRACEPTION_DURATION` | DOUBLE | NOT NULL |  | Duration of contraception use prior to pregnancy, in years |
| 5 | `CONTRACEPTION_IND` | DOUBLE | NOT NULL |  | Indicates whether hormonal contraception was in use at the time of conception |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LMP_SYMPTOMS_TXT` | VARCHAR(255) |  |  | Description of symptoms that may have accompanied last menstrual period prior to pregnancy |
| 8 | `MENARCHE_AGE` | DOUBLE | NOT NULL |  | Age at menarche, in years |
| 9 | `MENSTRUAL_FREQ` | DOUBLE | NOT NULL |  | Frequency of typical menstrual cycle, in days |
| 10 | `PREGNANCY_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 11 | `PREGNANCY_ESTIMATE_ID` | DOUBLE | NOT NULL | FK→ | The pregnancy estimate to which these details are related |
| 12 | `PREGNANCY_TEST_DT_TM` | DATETIME |  |  | Date of home pregnancy test |
| 13 | `PRIOR_MENSES_DT_TM` | DATETIME |  |  | Date of last menses prior to LMP |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREGNANCY_ESTIMATE_ID` | [PREGNANCY_ESTIMATE](PREGNANCY_ESTIMATE.md) | `PREGNANCY_ESTIMATE_ID` |

