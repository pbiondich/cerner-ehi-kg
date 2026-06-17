# HM_EXPECT_SAT

> This is a listing of all the Health Expectation Series, Expectation, and Step Satisfiers.

**Description:** This is a listing of all the Health Expectation Series and Step Satisfiers.  
**Table type:** REFERENCE  
**Primary key:** `EXPECT_SAT_ID`  
**Columns:** 30  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ENTRY_ID` | DOUBLE | NOT NULL |  | The ID of the entry type from ENTRY_NAME |
| 8 | `ENTRY_NAME` | VARCHAR(30) | NOT NULL |  | The table name corresponding to the ENTRY_ID source |
| 9 | `ENTRY_NBR` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. The entry ID for the specified entry type. This can be a PowerForm form identifier, a Clinical Note document identifier, an order identifier, or an order set identifier. In some cases, this may be the same as the Satisfier Id. |
| 10 | `ENTRY_TYPE_CD` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. A code value from code set that indicates the method of satisfier entry available from within the Health Maintenance View. Possible conversations are a PowerForm, Clinical Note, Scratch Pad, or EasyScript. Future design will also include PowerNote. |
| 11 | `ENTRY_VALUE` | VARCHAR(255) |  |  | This is a string identifier of the entry type identified by the ENTRY_TYPE_CD. |
| 12 | `EXPECT_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECTATION table that indicates which expectation this record corresponds to. |
| 13 | `EXPECT_SAT_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify an expectation satisfier. |
| 14 | `EXPECT_SAT_NAME` | VARCHAR(250) |  |  | This is the name for the expectation satisfier. |
| 15 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation Satisfier History table for this satisfier. |
| 16 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis to associate to this satisfier. Foreign key value from the NOMENCLATURE table |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the satisfier type from parent_entity_name. It is 0 if the satisfier is manual or a clinical event. |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table name of the parent_entity_id source |
| 19 | `PARENT_NBR` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. This is the ID of the satisfier type identified by the PARENT_TYPE_FLAG. If the PARENT_TYPE_FLAG is 2 (indicating a manual satisfier), this field will be 0. |
| 20 | `PARENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | OBSOLETE on Feature 144577 and subsequent. This is a flag indicating what type the satisfier is. It can be a clinical event (0), order or order set (1), or it can be a manual satisfier (2). |
| 21 | `PARENT_VALUE` | VARCHAR(255) |  |  | This is a string identifier of the satisfier type identified by the PARENT_TYPE_FLAG. |
| 22 | `PENDING_DURATION` | DOUBLE | NOT NULL |  | This is the duration after the satisfier is placed in which the expectation will be in a pending status. This field is only valid for order satisfiers. If the order permanently satisfies the step, this value will be 0. |
| 23 | `SATISFIED_DURATION` | DOUBLE | NOT NULL |  | This is the duration that a satisfier will satisfy an expectation. This value is only valid for expectations with an infinite number of steps. |
| 24 | `SATISFIER_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies a satisfier. Multiple satisfiers can have the same meaning if they belong to different expectations. Cerner standard satisfiers have a meaning that begins with "CERNER" and client defined expectations are prohibited from utilizing that meaning prefix. |
| 25 | `SEQ_NBR` | DOUBLE | NOT NULL |  | This sequence number indicates the order in which the satisfiers should be displayed. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_ID` | [HM_EXPECT](HM_EXPECT.md) | `EXPECT_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `EXPECT_SAT_ID` |
| [HM_EXPECT_MOD_HIST](HM_EXPECT_MOD_HIST.md) | `EXPECT_SAT_ID` |
| [HM_EXPECT_SAT_HIST](HM_EXPECT_SAT_HIST.md) | `EXPECT_SAT_ID` |
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `EXPECT_SAT_ID` |

