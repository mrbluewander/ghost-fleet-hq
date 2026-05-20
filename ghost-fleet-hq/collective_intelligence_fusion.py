#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
幽靈艦隊集體智能融合系統 (CIFS)
Collective Intelligence Fusion System

作者: Manus Agent
版本: 1.0.0
日期: 2026-04-28
"""

import asyncio
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import statistics
from datetime import datetime

# ==================== 配置 ====================

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] CIFS.%(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('CollectiveIntelligence')


# ==================== 數據結構 ====================

class TaskComplexity(Enum):
    """任務複雜度分類"""
    SIMPLE = "simple"      # 簡單任務 (< 0.3)
    MEDIUM = "medium"      # 中等複雜 (0.3-0.7)
    COMPLEX = "complex"    # 複雜任務 (>= 0.7)


class BrainType(Enum):
    """大腦類型"""
    GEMINI = "gemini"          # Google Gemini
    GROK = "grok"              # xAI Grok
    DEEPSEEK = "deepseek"      # DeepSeek v4
    KIMI = "kimi"              # Moonshot Kimi
    GPT = "gpt"                # OpenAI GPT
    CLAUDE = "claude"          # Anthropic Claude
    MYTHOS = "mythos"          # 新服務 Mythos


@dataclass
class BrainResponse:
    """大腦的回應"""
    brain_type: BrainType
    answer: str
    confidence: float  # 0-1
    reasoning: str
    processing_time: float
    error: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            "brain": self.brain_type.value,
            "answer": self.answer,
            "confidence": self.confidence,
            "reasoning": self.reasoning,
            "processing_time": self.processing_time,
            "error": self.error
        }


@dataclass
class FusionResult:
    """融合結果"""
    final_answer: str
    confidence_score: float
    consistency_score: float
    reasoning: str
    all_responses: List[BrainResponse]
    fusion_method: str
    quality_assessment: Dict[str, float]
    
    def to_dict(self) -> Dict:
        return {
            "final_answer": self.final_answer,
            "confidence_score": self.confidence_score,
            "consistency_score": self.consistency_score,
            "reasoning": self.reasoning,
            "fusion_method": self.fusion_method,
            "quality_assessment": self.quality_assessment,
            "all_responses": [r.to_dict() for r in self.all_responses],
            "timestamp": datetime.now().isoformat()
        }


# ==================== 大腦連接器 ====================

class BrainConnector:
    """大腦連接器基類"""
    
    def __init__(self, brain_type: BrainType, api_key: Optional[str] = None):
        self.brain_type = brain_type
        self.api_key = api_key
        self.logger = logging.getLogger(f'Brain.{brain_type.value}')
    
    async def think(self, prompt: str) -> BrainResponse:
        """思考 - 由子類實現"""
        raise NotImplementedError


class GeminiBrain(BrainConnector):
    """Gemini 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """Gemini 思考"""
        import time
        start_time = time.time()
        
        try:
            # 模擬 Gemini API 調用
            # 實際實現需要調用真實的 Gemini API
            await asyncio.sleep(0.1)  # 模擬 API 延遲
            
            answer = f"[Gemini 視角] {prompt[:50]}... → 多模態分析結果"
            
            return BrainResponse(
                brain_type=BrainType.GEMINI,
                answer=answer,
                confidence=0.85,
                reasoning="基於多模態理解和實時信息",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"Gemini 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.GEMINI,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class GrokBrain(BrainConnector):
    """Grok 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """Grok 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[Grok 實時視角] {prompt[:50]}... → 實時市場數據分析"
            
            return BrainResponse(
                brain_type=BrainType.GROK,
                answer=answer,
                confidence=0.80,
                reasoning="基於實時數據和 Twitter 集成",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"Grok 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.GROK,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class DeepSeekBrain(BrainConnector):
    """DeepSeek 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """DeepSeek 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[DeepSeek 技術視角] {prompt[:50]}... → 代碼和邏輯分析"
            
            return BrainResponse(
                brain_type=BrainType.DEEPSEEK,
                answer=answer,
                confidence=0.90,
                reasoning="基於強大的代碼能力和邏輯推理",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"DeepSeek 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.DEEPSEEK,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class KimiBrain(BrainConnector):
    """Kimi 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """Kimi 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[Kimi 知識視角] {prompt[:50]}... → 長文本知識提取"
            
            return BrainResponse(
                brain_type=BrainType.KIMI,
                answer=answer,
                confidence=0.82,
                reasoning="基於長文本處理和中文理解",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"Kimi 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.KIMI,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class GPTBrain(BrainConnector):
    """GPT 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """GPT 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[GPT 創意視角] {prompt[:50]}... → 通用創意分析"
            
            return BrainResponse(
                brain_type=BrainType.GPT,
                answer=answer,
                confidence=0.88,
                reasoning="基於通用能力和創意生成",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"GPT 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.GPT,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class ClaudeBrain(BrainConnector):
    """Claude 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """Claude 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[Claude 審核視角] {prompt[:50]}... → 深度邏輯推理"
            
            return BrainResponse(
                brain_type=BrainType.CLAUDE,
                answer=answer,
                confidence=0.92,
                reasoning="基於深度推理和邏輯嚴密性",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"Claude 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.CLAUDE,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


class MythosBrain(BrainConnector):
    """Mythos 大腦連接器"""
    
    async def think(self, prompt: str) -> BrainResponse:
        """Mythos 思考"""
        import time
        start_time = time.time()
        
        try:
            await asyncio.sleep(0.1)
            
            answer = f"[Mythos 探索視角] {prompt[:50]}... → 創新領域分析"
            
            return BrainResponse(
                brain_type=BrainType.MYTHOS,
                answer=answer,
                confidence=0.75,
                reasoning="基於新服務的創新能力",
                processing_time=time.time() - start_time
            )
        except Exception as e:
            self.logger.error(f"Mythos 思考失敗: {e}")
            return BrainResponse(
                brain_type=BrainType.MYTHOS,
                answer="",
                confidence=0.0,
                reasoning="",
                processing_time=time.time() - start_time,
                error=str(e)
            )


# ==================== 任務分類器 ====================

class TaskClassifier:
    """任務複雜度分類器"""
    
    @staticmethod
    def classify(prompt: str) -> Tuple[TaskComplexity, float]:
        """
        分類任務複雜度
        
        返回: (複雜度分類, 複雜度評分 0-1)
        """
        # 簡單啟發式規則
        complexity_score = 0.0
        
        # 基於提示詞長度
        complexity_score += min(len(prompt) / 1000, 0.3)
        
        # 基於關鍵詞
        complex_keywords = [
            "分析", "評估", "比較", "策略", "建議",
            "複雜", "深度", "系統", "整合", "優化"
        ]
        
        for keyword in complex_keywords:
            if keyword in prompt:
                complexity_score += 0.1
        
        # 限制在 0-1 之間
        complexity_score = min(complexity_score, 1.0)
        
        # 分類
        if complexity_score < 0.3:
            return TaskComplexity.SIMPLE, complexity_score
        elif complexity_score < 0.7:
            return TaskComplexity.MEDIUM, complexity_score
        else:
            return TaskComplexity.COMPLEX, complexity_score


# ==================== 智能路由器 ====================

class IntelligentRouter:
    """智能路由器 - 根據任務選擇大腦"""
    
    @staticmethod
    def select_brains(
        complexity: TaskComplexity,
        prompt: str
    ) -> List[BrainType]:
        """
        根據複雜度選擇大腦
        """
        if complexity == TaskComplexity.SIMPLE:
            # 簡單任務 - 選擇最快的單一大腦
            if "代碼" in prompt or "程序" in prompt:
                return [BrainType.DEEPSEEK]
            elif "實時" in prompt or "市場" in prompt:
                return [BrainType.GROK]
            elif "文檔" in prompt or "長文本" in prompt:
                return [BrainType.KIMI]
            else:
                return [BrainType.GEMINI]
        
        elif complexity == TaskComplexity.MEDIUM:
            # 中等複雜 - 分工協作
            if "代碼" in prompt:
                return [BrainType.DEEPSEEK, BrainType.CLAUDE]
            elif "文檔" in prompt:
                return [BrainType.KIMI, BrainType.CLAUDE]
            elif "創意" in prompt:
                return [BrainType.GPT, BrainType.CLAUDE]
            else:
                return [BrainType.GEMINI, BrainType.CLAUDE, BrainType.DEEPSEEK]
        
        else:  # COMPLEX
            # 複雜任務 - 融合協作 (全部大腦)
            return [
                BrainType.GEMINI,
                BrainType.GROK,
                BrainType.DEEPSEEK,
                BrainType.KIMI,
                BrainType.GPT,
                BrainType.CLAUDE,
                BrainType.MYTHOS
            ]


# ==================== 融合引擎 ====================

class FusionEngine:
    """集體智能融合引擎"""
    
    def __init__(self):
        self.logger = logging.getLogger('FusionEngine')
        self.brain_weights = {
            BrainType.CLAUDE: 1.0,      # 最可信
            BrainType.DEEPSEEK: 0.95,
            BrainType.GPT: 0.90,
            BrainType.GEMINI: 0.85,
            BrainType.KIMI: 0.80,
            BrainType.GROK: 0.75,
            BrainType.MYTHOS: 0.70     # 新服務
        }
    
    def voting_mechanism(self, responses: List[BrainResponse]) -> Dict[str, Any]:
        """投票機制"""
        # 提取答案
        answers = [r.answer for r in responses if not r.error]
        
        if not answers:
            return {"winner": None, "votes": {}, "consensus": 0.0}
        
        # 計算投票
        vote_count = {}
        for answer in answers:
            # 簡化：使用答案的前 50 個字符作為投票單位
            key = answer[:50]
            vote_count[key] = vote_count.get(key, 0) + 1
        
        # 找出最多票的答案
        winner = max(vote_count.items(), key=lambda x: x[1])[0]
        total_votes = len(answers)
        consensus = vote_count[winner] / total_votes if total_votes > 0 else 0.0
        
        return {
            "winner": winner,
            "votes": vote_count,
            "consensus": consensus
        }
    
    def weighted_average(self, responses: List[BrainResponse]) -> Tuple[float, str]:
        """加權平均信心度"""
        total_weight = 0.0
        weighted_confidence = 0.0
        reasoning_parts = []
        
        for response in responses:
            if not response.error:
                weight = self.brain_weights.get(response.brain_type, 0.5)
                weighted_confidence += response.confidence * weight
                total_weight += weight
                reasoning_parts.append(
                    f"{response.brain_type.value}: {response.reasoning}"
                )
        
        avg_confidence = weighted_confidence / total_weight if total_weight > 0 else 0.0
        reasoning = " | ".join(reasoning_parts)
        
        return avg_confidence, reasoning
    
    def consistency_check(self, responses: List[BrainResponse]) -> float:
        """一致性檢查"""
        if not responses:
            return 0.0
        
        # 計算信心度的標準差
        confidences = [r.confidence for r in responses if not r.error]
        
        if len(confidences) < 2:
            return 1.0
        
        mean_confidence = statistics.mean(confidences)
        std_dev = statistics.stdev(confidences)
        
        # 轉換為一致性分數 (0-1)
        consistency = 1.0 / (1.0 + std_dev)
        
        return consistency
    
    async def fuse(self, responses: List[BrainResponse]) -> FusionResult:
        """融合所有回應"""
        self.logger.info(f"開始融合 {len(responses)} 個大腦的回應")
        
        # 1. 投票機制
        voting_result = self.voting_mechanism(responses)
        
        # 2. 加權平均
        weighted_confidence, reasoning = self.weighted_average(responses)
        
        # 3. 一致性檢查
        consistency_score = self.consistency_check(responses)
        
        # 4. 生成最終答案
        final_answer = voting_result.get("winner", "無法達成共識")
        
        # 5. 質量評估
        quality_assessment = {
            "voting_consensus": voting_result["consensus"],
            "weighted_confidence": weighted_confidence,
            "consistency_score": consistency_score,
            "success_rate": len([r for r in responses if not r.error]) / len(responses)
        }
        
        # 6. 計算最終信心度
        final_confidence = (
            voting_result["consensus"] * 0.4 +
            weighted_confidence * 0.4 +
            consistency_score * 0.2
        )
        
        result = FusionResult(
            final_answer=final_answer,
            confidence_score=final_confidence,
            consistency_score=consistency_score,
            reasoning=reasoning,
            all_responses=responses,
            fusion_method="voting + weighted_average + consistency_check",
            quality_assessment=quality_assessment
        )
        
        self.logger.info(f"融合完成 - 信心度: {final_confidence:.2%}")
        
        return result


# ==================== 集體智能系統 ====================

class CollectiveIntelligenceSystem:
    """幽靈艦隊集體智能融合系統"""
    
    def __init__(self):
        self.logger = logging.getLogger('CIFS')
        self.classifier = TaskClassifier()
        self.router = IntelligentRouter()
        self.fusion_engine = FusionEngine()
        
        # 初始化所有大腦連接器
        self.brains = {
            BrainType.GEMINI: GeminiBrain(BrainType.GEMINI),
            BrainType.GROK: GrokBrain(BrainType.GROK),
            BrainType.DEEPSEEK: DeepSeekBrain(BrainType.DEEPSEEK),
            BrainType.KIMI: KimiBrain(BrainType.KIMI),
            BrainType.GPT: GPTBrain(BrainType.GPT),
            BrainType.CLAUDE: ClaudeBrain(BrainType.CLAUDE),
            BrainType.MYTHOS: MythosBrain(BrainType.MYTHOS)
        }
        
        self.logger.info("🧠 幽靈艦隊集體智能系統已初始化")
    
    async def think(self, prompt: str) -> FusionResult:
        """
        集體智能思考
        
        流程:
        1. 分類任務複雜度
        2. 智能路由選擇大腦
        3. 並行調用大腦
        4. 融合決策
        5. 質量評估
        """
        self.logger.info(f"📝 接收任務: {prompt[:100]}...")
        
        # 1. 分類任務
        complexity, score = self.classifier.classify(prompt)
        self.logger.info(f"📊 任務複雜度: {complexity.value} (評分: {score:.2f})")
        
        # 2. 智能路由
        selected_brains = self.router.select_brains(complexity, prompt)
        self.logger.info(f"🧠 選擇大腦: {[b.value for b in selected_brains]}")
        
        # 3. 並行調用
        self.logger.info("💭 大腦並行思考中...")
        tasks = [
            self.brains[brain_type].think(prompt)
            for brain_type in selected_brains
        ]
        responses = await asyncio.gather(*tasks)
        
        # 4. 融合決策
        self.logger.info("🔄 融合決策中...")
        result = await self.fusion_engine.fuse(responses)
        
        # 5. 記錄結果
        self.logger.info(f"✅ 最終答案信心度: {result.confidence_score:.2%}")
        
        return result


# ==================== 主程序 ====================

async def main():
    """主程序"""
    print("=" * 60)
    print("🎖️  幽靈艦隊集體智能融合系統 (CIFS)")
    print("=" * 60)
    print()
    
    # 初始化系統
    cifs = CollectiveIntelligenceSystem()
    print()
    
    # 測試案例
    test_cases = [
        "What is the capital of France?",  # 簡單任務
        "Generate a Python function to sort a list",  # 代碼任務
        "Analyze the impact of AI on global economy and provide strategic recommendations"  # 複雜任務
    ]
    
    for i, prompt in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"測試案例 {i}: {prompt[:50]}...")
        print(f"{'='*60}")
        
        result = await cifs.think(prompt)
        
        print(f"\n📌 最終答案:")
        print(f"   {result.final_answer}")
        print(f"\n📊 質量評估:")
        for key, value in result.quality_assessment.items():
            print(f"   {key}: {value:.2%}")
        print(f"\n💡 推理過程:")
        print(f"   {result.reasoning[:200]}...")
        print()
    
    print(f"\n{'='*60}")
    print("✅ 集體智能系統測試完成")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    asyncio.run(main())
